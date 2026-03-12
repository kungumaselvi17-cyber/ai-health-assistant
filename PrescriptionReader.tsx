import { useState } from 'react';
import { Upload, FileText, Loader2, CheckCircle, XCircle } from 'lucide-react';

const API_URL = 'http://localhost:5000';

interface AnalysisResult {
  medications_found: Array<{ name: string; description: string }>;
  instructions: string[];
  warnings: string[];
  simplified_text: string;
}

export default function PrescriptionReader() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [extractedText, setExtractedText] = useState<string>('');
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [uploadStatus, setUploadStatus] = useState<'idle' | 'success' | 'error'>('idle');

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      setPreviewUrl(URL.createObjectURL(file));
      setExtractedText('');
      setAnalysis(null);
      setUploadStatus('idle');
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    setIsUploading(true);
    setUploadStatus('idle');

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch(`${API_URL}/api/upload-prescription`, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (data.success) {
        setExtractedText(data.extracted_text);
        setUploadStatus('success');
        analyzeText(data.extracted_text);
      } else {
        setUploadStatus('error');
      }
    } catch (error) {
      setUploadStatus('error');
    } finally {
      setIsUploading(false);
    }
  };

  const analyzeText = async (text: string) => {
    setIsAnalyzing(true);

    try {
      const response = await fetch(`${API_URL}/api/analyze-prescription`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setAnalysis(data.analysis);
    } catch (error) {
      console.error('Analysis error:', error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="bg-gradient-to-r from-emerald-500 to-teal-600 text-white p-4">
        <div className="flex items-center gap-2">
          <FileText className="w-6 h-6" />
          <h2 className="text-xl font-semibold">Prescription Reader</h2>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
          <input
            type="file"
            accept="image/*,.pdf"
            onChange={handleFileSelect}
            className="hidden"
            id="file-upload"
          />
          <label
            htmlFor="file-upload"
            className="cursor-pointer flex flex-col items-center gap-2"
          >
            <Upload className="w-12 h-12 text-gray-400" />
            <p className="text-sm text-gray-600">
              Click to upload prescription image
            </p>
            <p className="text-xs text-gray-500">PNG, JPG, JPEG, or PDF</p>
          </label>
        </div>

        {selectedFile && (
          <div className="space-y-4">
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-2">
                <FileText className="w-5 h-5 text-teal-600" />
                <span className="text-sm font-medium text-gray-700">
                  {selectedFile.name}
                </span>
              </div>
              {uploadStatus === 'success' && (
                <CheckCircle className="w-5 h-5 text-green-500" />
              )}
              {uploadStatus === 'error' && (
                <XCircle className="w-5 h-5 text-red-500" />
              )}
            </div>

            {previewUrl && (
              <div className="rounded-lg overflow-hidden border border-gray-200">
                <img
                  src={previewUrl}
                  alt="Prescription preview"
                  className="w-full h-64 object-contain bg-gray-50"
                />
              </div>
            )}

            <button
              onClick={handleUpload}
              disabled={isUploading}
              className="w-full px-4 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors flex items-center justify-center gap-2"
            >
              {isUploading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Processing...
                </>
              ) : (
                <>
                  <Upload className="w-5 h-5" />
                  Read Prescription
                </>
              )}
            </button>
          </div>
        )}

        {extractedText && (
          <div className="space-y-4">
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <h3 className="font-semibold text-blue-900 mb-2">Extracted Text</h3>
              <p className="text-sm text-blue-800 whitespace-pre-wrap">
                {extractedText}
              </p>
            </div>

            {isAnalyzing && (
              <div className="flex items-center justify-center gap-2 text-gray-600">
                <Loader2 className="w-5 h-5 animate-spin" />
                <span>Analyzing prescription...</span>
              </div>
            )}

            {analysis && (
              <div className="space-y-3">
                {analysis.medications_found.length > 0 && (
                  <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                    <h3 className="font-semibold text-green-900 mb-2">
                      Medications Found
                    </h3>
                    <ul className="space-y-2">
                      {analysis.medications_found.map((med, idx) => (
                        <li key={idx} className="text-sm">
                          <span className="font-medium text-green-800">
                            {med.name}:
                          </span>{' '}
                          <span className="text-green-700">{med.description}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {analysis.instructions.length > 0 && (
                  <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
                    <h3 className="font-semibold text-purple-900 mb-2">
                      Dosage Instructions
                    </h3>
                    <ul className="list-disc list-inside space-y-1">
                      {analysis.instructions.map((instruction, idx) => (
                        <li key={idx} className="text-sm text-purple-800">
                          {instruction}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {analysis.warnings.length > 0 && (
                  <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                    <h3 className="font-semibold text-yellow-900 mb-2">
                      Important Warnings
                    </h3>
                    <ul className="list-disc list-inside space-y-1">
                      {analysis.warnings.map((warning, idx) => (
                        <li key={idx} className="text-sm text-yellow-800">
                          {warning}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {analysis.simplified_text && (
                  <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
                    <h3 className="font-semibold text-gray-900 mb-2">
                      Simplified Text
                    </h3>
                    <p className="text-sm text-gray-700 whitespace-pre-wrap">
                      {analysis.simplified_text}
                    </p>
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
