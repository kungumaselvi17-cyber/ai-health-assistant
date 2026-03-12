import { useState } from 'react';
import { Heart, MessageSquare, FileText } from 'lucide-react';
import ChatInterface from './components/ChatInterface';
import PrescriptionReader from './components/PrescriptionReader';

function App() {
  const [activeTab, setActiveTab] = useState<'chat' | 'prescription'>('chat');

  return (
    <div className="min-h-screen bg-gradient-to-br from-teal-50 via-emerald-50 to-cyan-50">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8 text-center">
          <div className="flex items-center justify-center gap-3 mb-3">
            <Heart className="w-10 h-10 text-teal-600" />
            <h1 className="text-4xl font-bold text-gray-800">AI Health Assistant</h1>
          </div>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Get general health information and read prescriptions with AI-powered assistance
          </p>
          <p className="text-sm text-gray-500 mt-2">
            Disclaimer: This is for informational purposes only. Always consult healthcare professionals for medical advice.
          </p>
        </div>

        <div className="max-w-7xl mx-auto">
          <div className="bg-white rounded-lg shadow-md mb-6 p-1 flex gap-2">
            <button
              onClick={() => setActiveTab('chat')}
              className={`flex-1 py-3 px-6 rounded-lg font-medium transition-all flex items-center justify-center gap-2 ${
                activeTab === 'chat'
                  ? 'bg-teal-500 text-white shadow-sm'
                  : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              <MessageSquare className="w-5 h-5" />
              Health Chat
            </button>
            <button
              onClick={() => setActiveTab('prescription')}
              className={`flex-1 py-3 px-6 rounded-lg font-medium transition-all flex items-center justify-center gap-2 ${
                activeTab === 'prescription'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              <FileText className="w-5 h-5" />
              Prescription Reader
            </button>
          </div>

          <div className="h-[600px]">
            {activeTab === 'chat' ? <ChatInterface /> : <PrescriptionReader />}
          </div>
        </div>

        <div className="mt-8 text-center">
          <div className="bg-white rounded-lg shadow-md p-6 max-w-3xl mx-auto">
            <h2 className="text-xl font-semibold text-gray-800 mb-3">How to Use</h2>
            <div className="grid md:grid-cols-2 gap-4 text-left">
              <div>
                <h3 className="font-medium text-teal-600 mb-2">Health Chat</h3>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>Ask questions about symptoms</li>
                  <li>Get general health advice</li>
                  <li>Learn about medications</li>
                  <li>Understand wellness topics</li>
                </ul>
              </div>
              <div>
                <h3 className="font-medium text-emerald-600 mb-2">Prescription Reader</h3>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>Upload prescription images</li>
                  <li>Extract text from prescriptions</li>
                  <li>Get simplified explanations</li>
                  <li>Understand medication details</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
