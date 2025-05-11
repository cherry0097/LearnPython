import React from "react";
import { useForm } from "react-hook-form";

export default function Login() {
  const { register, handleSubmit } = useForm();
  const onSubmit = async (data) => {
    const formData = new URLSearchParams();
    formData.append("username", data.username);
    formData.append("password", data.password);
    console.log(formData)

    try {
      const response = await fetch("http://127.0.0.1:8000/post/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData.toString(),
      });

      const result = await response.json();
      console.log("Login response:", result);

      if (result.access_token) {
        // ✅ Save token to localStorage
        localStorage.setItem("token", result.access_token);
        // Optional: redirect to secret page
        window.location.href = "/secretpage";
      } else {
        alert("Login failed. No token received.");
      }
    } catch (error) {
      console.error("Login error:", error);
    }
  };
  return (
    <div className="bg-purple-800 ml-15 mr-200 mt-5 border-2 rounded-4xl border-green-800 pt-2.5 pb-45">
      <div className="flex justify-center text-2xl text-white">LOG IN</div>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col ml-10 mr-10"
      >
        <label className="my-2 text-white">Username:</label>
        <input
          type="text"
          {...register("username")}
          className="bg-white my-2"
        />
        <label className="my-2 text-white">Password:</label>
        <input
          type="password"
          {...register("password")}
          className="bg-white my-2"
        />
        <input
          type="submit"
          className="mt-5 border-2 rounded-2xl bg-indigo-400 hover:bg-blue-700 hover:text-white hover:cursor-pointer"
        />
      </form>
    </div>
  );
}
