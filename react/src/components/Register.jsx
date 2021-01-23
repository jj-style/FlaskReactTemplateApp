import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import api from "../services/api";
import { useAuth } from "../services/auth";

const Register = () => {
  const [state, setState] = useState({ username: "", email: "", password: "" });
  const [error, setError] = useState(null);

  const inputChanged = (e) => {
    e.persist();
    setState((currState) => ({ ...currState, [e.target.id]: e.target.value }));
  };

  let history = useHistory();
  const { setToken } = useAuth();

  const register = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch(api + "/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: state.username,
          email: state.email,
          password: state.password,
        }),
      });
      if (!res.ok) throw new Error(await res.text());
      history.replace("/login");
    } catch (err) {
      setError(err.toString());
    }
  };

  return (
    <div>
      <form onSubmit={register}>
        <div>
          <input
            type="text"
            id="username"
            placeholder="enter username"
            value={state.username}
            onChange={inputChanged}
          />
          <input
            type="email"
            id="email"
            placeholder="enter email"
            value={state.email}
            onChange={inputChanged}
          />
          <input
            type="password"
            id="password"
            placeholder="enter password"
            value={state.password}
            onChange={inputChanged}
          />
        </div>
        {error && (
          <p role="alert" style={{ color: "red" }}>
            {error}
          </p>
        )}
        <div>
          <Link to="/login">Already signed up? Login here</Link>
        </div>
        <button type="submit">Sign up</button>
      </form>
    </div>
  );
};

export default Register;
