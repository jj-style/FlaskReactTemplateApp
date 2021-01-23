import { useHistory } from "react-router-dom";
import { useAuth } from "../services/auth";
import api from "../services/api";

function AuthButton() {
  const history = useHistory();
  const { token, removeToken } = useAuth();

  return token ? (
    <p>
      Welcome!{" "}
      <button
        onClick={() => {
          fetch(`${api}/logout`, { headers: { "X-Auth": token } }).then(() => {
            removeToken(() => history.push("/"));
          });
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
