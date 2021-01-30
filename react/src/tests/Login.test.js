import { expect } from "chai";
import { mount } from "enzyme";
import { act } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import Login from "../components/Login";
import { AuthProvider } from "../services/auth";

const LoginWrapped = (
  <BrowserRouter>
    <AuthProvider>
      <Login />
    </AuthProvider>
  </BrowserRouter>
);

describe("<Login/>", () => {
  beforeEach(() => {
    fetch.resetMocks();
  });

  it("renders login component without crashing", () => {
    mount(LoginWrapped);
  });

  it("contains a form with fields for username and password", () => {
    const wrapper = mount(LoginWrapped);
    expect(wrapper.find("#loginForm")).to.have.lengthOf(1);
    expect(wrapper.find("input[type='text']")).to.have.lengthOf(1);
    expect(wrapper.find("input[type='password']")).to.have.lengthOf(1);
  });

  it("makes a post request to login when form is submitted", async () => {
    fetch.mockResponse(JSON.stringify({ token: "aaa" }));
    const wrapper = mount(LoginWrapped);
    wrapper.setState({ username: "foo", password: "bar" });
    await act(async () => {
      wrapper.find("form").simulate("submit");
    });
    expect(fetch.mock.calls.length).to.equal(1);
    expect(fetch.mock.calls[0][0]).to.equal("http://localhost:8080/login");
  });
});
