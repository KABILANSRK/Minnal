import React, { useEffect, useState } from "react";
import './App.css'

const App = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://minnal-u6z8.onrender.com/api/schedule")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((fetchedData) => setData(fetchedData))
      .catch((err) => setError(err));
  }, []);

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!data) {
    return <div>Loading...</div>;
  }

  if (!data.success) {
    return <div>{data.message}</div>;
  }

  return (
    <>
      <h1>Minnal ⚡</h1>
      <h4>Powercut Areas:</h4>
      <pre style={{ whiteSpace: "pre-wrap" }}>{data.data.info}</pre>
      {data.data.source && (
        <p>
          Source:{" "}
          <a href={data.data.source} target="_blank" rel="noopener noreferrer">
            {data.data.source}
          </a>
        </p>
      )}
    </>
  );
};

export default App;
