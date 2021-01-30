import { mount } from "enzyme";
import { BrowserRouter } from "react-router-dom";
import App from "../App";
import { AuthProvider } from "../services/auth";

test("renders app without crashing", () => {
  const app = (
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  );
  mount(app);
});
