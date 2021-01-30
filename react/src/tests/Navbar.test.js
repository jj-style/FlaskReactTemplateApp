import { mount } from "enzyme";
import { expect } from "chai";
import { BrowserRouter, NavLink } from "react-router-dom";
import Navbar from "../components/Navbar";
import { AuthProvider } from "../services/auth";

const WrappedNavbar = (
  <BrowserRouter>
    <AuthProvider>
      <Navbar />
    </AuthProvider>
  </BrowserRouter>
);

const WrappedNavbarWithToken = (
  <BrowserRouter>
    <AuthProvider defaultState={{ token: "aaa" }}>
      <Navbar />
    </AuthProvider>
  </BrowserRouter>
);

describe("<Navbar />", () => {
  it("renders without a navbar without crashing", () => {
    mount(WrappedNavbar);
  });

  it("contains a navbar container", () => {
    const wrapper = mount(WrappedNavbar);
    expect(wrapper.find("#nav")).to.have.lengthOf(1);
  });

  it("contains 3 links when not logged in", () => {
    const wrapper = mount(WrappedNavbar);
    expect(wrapper.find(NavLink)).to.have.lengthOf(3);
  });

  it("contains 2 links when logged in", () => {
    const wrapper = mount(WrappedNavbarWithToken);
    expect(wrapper.find(NavLink)).to.have.lengthOf(2);
  });
});
