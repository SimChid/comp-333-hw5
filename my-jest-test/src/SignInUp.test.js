import React from "react" ;
import {render,screen,fireEvent, getByTestId} from "@testing-library/react" ;
import SignInUp from "./SignInUp";
import "@testing-library/jest-dom" ;
import { BrowserRouter } from "react-router-dom";
import userEvent from '@testing-library/user-event';
import { act } from "react-dom/test-utils";
//import "@testing-library/jest-dom/extend-expect";

describe("Initial Page", () => {
  // "it()" is the same as "test()", i.e., just an indentifier of a test.
  // we can give it any description we like, e.g., here "renders the input field"
  it("renders the header", () => {
    render(<SignInUp />);
    const inputElement = screen.getByRole("information");
    // The assertion listed here is a part of jest-dom, which is not imported by
    // testing-library by default. We expect the form field to be rendered in
    // the DOM.
    expect(inputElement).toBeInTheDocument();
  });
  it("renders the login button", () => {
    render(<SignInUp />);
    const inputElement = screen.getByRole('LogInButton')
    // The assertion listed here is a part of jest-dom, which is not imported by
    // testing-library by default. We expect the form field to be rendered in
    // the DOM.
    expect(inputElement).toBeInTheDocument();
  });
  it("renders the sign up button", () => {
    render(<SignInUp />);
    const inputElement = screen.getByRole('SignUpButton')
    // The assertion listed here is a part of jest-dom, which is not imported by
    // testing-library by default. We expect the form field to be rendered in
    // the DOM.
    expect(inputElement).toBeInTheDocument();
  });
  it("login button renders proper elements", () => {
    render(<SignInUp />) ;
    const logInButton = screen.getByTestId("logInButton") ;
    fireEvent.click(logInButton) ; // Testing the button click works (2b/c)
    const logInForm = screen.getByRole('LogInHandler') ;
    const logInInfo = screen.getByRole('Info') ;
    expect(logInForm).toBeInTheDocument() ;
    expect(logInInfo).toBeInTheDocument() ;
  }) ;
  it("sign up button renders proper elements", () => {
    render(<SignInUp />) ;
    const signUpButton = screen.getByTestId("signUpButton") ;
    fireEvent.click(signUpButton) ;
    const logInForm = screen.getByRole('SignUpHandler') ;
    expect(logInForm).toBeInTheDocument() ;
  }) ;
});

describe("Logging In", () => {
  it("Login works properly", async() => {
    render(
      <BrowserRouter>
        <SignInUp />
      </BrowserRouter>
    ) ;
    const logInButton = screen.getByTestId("logInButton") ;
    fireEvent.click(logInButton) ;

    const usernameElement = screen.getByPlaceholderText("username") ;
    const passwordElement = screen.getByPlaceholderText("password") ;
    fireEvent.change(usernameElement,{target : {value : 'aaron'}}) ;
    fireEvent.change(passwordElement,{target : {value : 'strongpassword'}}) ;
    expect(usernameElement.value).toBe('aaron') ;
    expect(passwordElement.value).toBe('strongpassword') ;
    
  }) ;
});
  
