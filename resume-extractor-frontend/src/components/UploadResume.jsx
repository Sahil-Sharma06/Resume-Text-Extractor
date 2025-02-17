import { useState } from "react";
import axios from "axios";

export default function UploadResume() {
  const [file, setFile] = useState(null);
  const [structuredData, setStructuredData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file first.");
      return;
    }

    setLoading(true);
    setError("");
    setStructuredData(null);

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/", // Django API
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );
      setStructuredData(response.data.structured_resume);
    } catch (err) {
      setError("Error uploading file. Make sure backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-6 bg-white dark:bg-gray-900 dark:text-white shadow-lg rounded-lg mt-10 transition-all duration-300">
      <h1 className="text-3xl font-bold mb-6 text-center">Resume Extractor</h1>

      <div className="flex flex-col items-center space-y-4">
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="border border-gray-300 dark:border-gray-700 rounded p-2 w-full bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white"
        />

        <button
          onClick={handleUpload}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading ? "Uploading..." : "Upload & Extract"}
        </button>
      </div>

      {error && <p className="text-red-500 mt-3 text-center">{error}</p>}

      {structuredData && (
        <div className="mt-6">
          <h2 className="text-xl font-semibold">Extracted Resume Data</h2>
          <table className="min-w-full bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 mt-4 shadow-md rounded-md">
            <thead>
              <tr className="bg-gray-200 dark:bg-gray-700">
                <th className="text-left py-3 px-4 border-b">Section</th>
                <th className="text-left py-3 px-4 border-b">Content</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(structuredData).map(([key, value]) => (
                <tr key={key} className="border-b">
                  <td className="py-3 px-4 font-semibold">{key}</td>
                  <td className="py-3 px-4">{value || "N/A"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
