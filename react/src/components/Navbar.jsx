import React from "react";

import { NavLink } from "react-router-dom";
import { useAuth } from "../services/auth";

const Navbar = () => {
  const { token } = useAuth();
  return (
    <div id="nav">
      <NavLink to="/">Home</NavLink>
      <NavLink to="/posts">Posts</NavLink>
      {!token && <NavLink to="/login">Login</NavLink>}
    </div>
  );
};

export default Navbar;
