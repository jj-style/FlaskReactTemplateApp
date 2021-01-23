import React, { useState } from "react";
import { Link, useHistory, useLocation } from "react-router-dom";
import api from "../services/api";
import { useAuth } from "../services/auth";

const Login = () => {
  const [state, setState] = useState({ username: "", password: "" });
  const [error, setError] = useState(null);

  const inputChanged = (e) => {
    e.persist();
    setState((currState) => ({ ...currState, [e.target.id]: e.target.value }));
  };

  let history = useHistory();
  let location = useLocation();
  const { setToken } = useAuth();

  let { from } = location.state || { from: { pathname: "/" } };

  const login = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch(api + "/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: state.username,
          password: state.password,
        }),
      });
      if (!res.ok) throw new Error(await res.text());
      const { token } = await res.json();
      setToken(token);
      history.replace(from);
    } catch (err) {
      setError(err.toString());
    }
  };

  return (
    <div>
      <p>You must log in to view the page at {from.pathname}</p>
      <form onSubmit={login}>
        <div>
          <input
            type="text"
            id="username"
            placeholder="enter username"
            value={state.username}
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
          <Link to="/register">New User? Register now</Link>
        </div>
        <button type="submit">Log in</button>
      </form>
    </div>
  );
};

export default Login;
