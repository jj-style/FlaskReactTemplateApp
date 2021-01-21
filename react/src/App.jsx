import React from "react";
import { Redirect, Route, Switch } from "react-router-dom";
import AuthButton from "./components/AuthButton";
import Home from "./components/Home";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import Posts from "./components/Posts";
import Register from "./components/Register";

import { useAuth } from "./services/auth";

const App = () => {
  return (
    <div className="App">
      <Navbar />
      <AuthButton />
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/register">
          <Register />
        </Route>
        <PrivateRoute path="/posts">
          <Posts />
        </PrivateRoute>
      </Switch>
    </div>
  );
};

// A wrapper for <Route> that redirects to the login
// screen if you're not yet authenticated.
function PrivateRoute({ children, ...rest }) {
  const { token } = useAuth();
  return (
    <Route
      {...rest}
      render={({ location }) =>
        token ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: location },
            }}
          />
        )
      }
    />
  );
}

export default App;
