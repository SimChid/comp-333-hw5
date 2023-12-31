import React from "react" ;
import {render,screen,fireEvent, getByTestId} from "@testing-library/react" ;
import CreateSongRating from "./createSongRating";
import "@testing-library/jest-dom" ;
import { BrowserRouter } from "react-router-dom";

describe("Rendering Tests", () => {

    
    it("renders the create rating form", () => {
        render(<BrowserRouter><CreateSongRating /></BrowserRouter>);
        const inputElement = screen.getByTestId("form");
        expect(inputElement).toBeInTheDocument();
    });
    
    it("renders the info", () => {
        render(<CreateSongRating />);
        const inputElement = screen.getByTestId("info");
        expect(inputElement).toBeInTheDocument();
    });

    it("renders the song rating list", () => {
        render(<CreateSongRating />);
        const inputElement = screen.getByTestId("songList");
        expect(inputElement).toBeInTheDocument();
    });

}) 