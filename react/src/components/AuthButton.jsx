import { useHistory } from "react-router-dom";
import { useAuth } from "../services/auth";

function AuthButton() {
  const history = useHistory();
  const { token, removeToken } = useAuth();

  return token ? (
    <p>
      Welcome!{" "}
      <button
        onClick={() => {
          removeToken(() => history.push("/"));
        }}
      >
        Sign out
      </button>
    </p>
  ) : (
    <p>You are not logged in.</p>
  );
}

export default AuthButton;
