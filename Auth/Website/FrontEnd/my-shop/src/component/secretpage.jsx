import React from "react";
import { useState, useEffect } from "react";

export default function Secretpage() {
  const [jsonData, setJsonData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      setError("No token found. Please log in.");
      return;
    }

    fetch("http://127.0.0.1:8000/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Unauthorized or fetch failed");
        }
        return res.json();
      })
      .then((data) => setJsonData([data])) // Wrap in array to map later
      .catch((err) => setError(err.message));
  }, []);

  if (error) {
    return <div className="text-red-500 text-center my-5">{error}</div>;
  }

  if (!jsonData) {
    return <div className="text-center my-5">Loading...</div>;
  }

  return (
    <div className="my-10 flex justify-center">
      <table className="border-2">
        <thead className="">
          <tr className="bg-yellow-400">
            <td className="border-2 px-1.5">User Name</td>
            <td className="border-2 px-1.5">First Name</td>
            <td className="border-2 px-1.5">Last Name</td>
            <td className="border-2 px-1.5">Salary</td>
          </tr>
        </thead>
        <tbody>
          {jsonData.map((data, index) => (
            <tr key={index}>
              <td className="border-2 px-1.5">{data.username}</td>
              <td className="border-2 px-1.5">{data.fname}</td>
              <td className="border-2 px-1.5">{data.lname}</td>
              <td className="border-2 px-1.5">{data.Salary}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
