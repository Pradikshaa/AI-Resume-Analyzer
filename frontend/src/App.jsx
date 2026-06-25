
import { useState } from "react"
import axios from "axios"
import "./App.css"

function App() {
  const [file, setFile] = useState(null)
  const [result, setResult] = useState(null)
  const [jobDescription, setJobDescription] = useState("")
  const [requiredSkills, setRequiredSkills] = useState("")


  const handleUpload = async () => {
    if (!file) {
      alert("Please select a resume")
      return
    }

    if (!jobDescription) {
      alert("Please enter job description")
      return
    }

    const formData = new FormData()
    formData.append("file", file)
    formData.append("job_description", jobDescription)
    formData.append("required_skills", requiredSkills)

    try {
      const response = await axios.post(
        "https://ai-resume-analyzer-wo70.onrender.com/upload",
        formData
      )
      setResult(response.data)
    } catch (error) {
      console.error(error)
      alert("Upload failed")
    }
  }

  return (
    <div className="app">
      <div className="header">
        <h1>ATS Analysis</h1>
        <p>AI-powered resume optimization</p>
      </div>

      <div className="upload-box">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <br /><br />

        <textarea
          placeholder="Paste Job Description here..."
          rows="8"
          cols="80"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />
        <br /><br />

<textarea
  placeholder="Enter required skills separated by commas"
  rows="4"
  cols="80"
  value={requiredSkills}
  onChange={(e) => setRequiredSkills(e.target.value)}
/>



        <br /><br />

        <button onClick={handleUpload}>Analyze Resume</button>
      </div>

      {result && (
        <div className="dashboard">
          <div className="left-panel">
            <div className="card">
              <h2>Analysis Summary</h2>
              <p>
                {result.matched_skills.length} strengths •{" "}
                {result.missing_skills.length} issues
              </p>
            </div>

            <div className="card">
              <h3>Strengths</h3>
              <ul>
                {result.matched_skills.map((skill, index) => (
                  <li key={index}>✔ {skill}</li>
                ))}
              </ul>
            </div>

            <div className="card">
              <h3>Areas for Improvement</h3>
              <ul>
                {result.missing_skills.map((skill, index) => (
                  <li key={index}>• Add {skill}</li>
                ))}
              </ul>
            </div>

            {result.suggestions && (
              <div className="card">
                <h3>Suggestions</h3>
                <ul>
                  {result.suggestions.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          <div className="right-panel">
            <div className="score-card">
              <h3>ATS Score</h3>
              <p>{result.ats_score}%</p>
            </div>

            <div className="score-card">
              <h3>Similarity Score</h3>
              <p>{result.similarity_score}%</p>
            </div>

            <div className="score-card">
              <h3>Total Skills Found</h3>
              <p>{result.skills.length}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
