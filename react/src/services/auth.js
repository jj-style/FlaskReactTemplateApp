import React, { useState, useContext, useEffect } from "react";

const AuthContext = React.createContext(null);

let initialToken = sessionStorage.getItem("token");
initialToken = initialToken === "null" ? null : initialToken;
// const initialToken = null;

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(initialToken);

  const removeToken = (cb) => {
    setToken(null);
    cb();
  };

  useEffect(() => {
    sessionStorage.setItem("token", token);
  }, [token]);

  const contextValue = { token, setToken, removeToken };
  return (
    <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
