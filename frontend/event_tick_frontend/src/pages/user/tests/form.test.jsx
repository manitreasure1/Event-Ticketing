import { screen, render, fireEvent, waitFor} from "@testing-library/dom";
import {jest} from '@jest/globals'
import userEvent from "@testing-library/user-event"
import { describe, it, expect } from 'jest';
import UserForm from "../form";

console.log = jest.fn()

describe("User Components",()=>{
    it("rendering form lable and input", ()=>{
        render(<UserForm/>)
        expect(screen.getByRole('legend', {name : /Login/i}).toBeInTheDocument());
        expect(screen.getByRole('legend', {name : /Sign Up/i}).toBeInTheDocument());

        expect(screen.getByLabelText(/first name/i).toBeInTheDocument());
        expect(screen.getByLabelText(/last name/i).toBeInTheDocument());


        expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
        expect(screen.getByRole('button', {name: /login/i})).toBeInTheDocument();

    })
    it("update user inputs on change",()=>{
        render(<UserForm/>)
        const firstName = screen.getByLabelText(/first name/);
        const lastName = screen.getByLabelText(/last name/);
        const email = screen.getByLabelText(/email/);
        const password = screen.getByLabelText(/password/);

        fireEvent.change(firstName, {target:{value: "Treas"}});
        fireEvent.change(lastName, {target:{value: "Mani"}});
        fireEvent.change(email, {target:{value: "example@mail.com"}});
        fireEvent.change(password, {target:{value: "password@@123"}});
    })
    it("Submits the form data",async ()=>{
        render(<UserForm/>)
        const firstName = screen.getByLabelText(/first name/);
        const lastName = screen.getByLabelText(/last name/);
        const email = screen.getByLabelText(/email/);
        const password = screen.getByLabelText(/password/);
        const submitButon = screen.getByRole('button', {name:/Login/i})
        userEvent.type(firstName, "Treas")
        userEvent.type(lastName, "Mani")
        userEvent.type(email, "example@email.com")
        userEvent.type(password, "password@@123")
        fireEvent.click(submitButon)

        await waitFor(()=>{
            expect(console.log).toHaveBeenCalledWith({
                firstname:"Treas",
                lastname : "Mani",
                email :"exampl@email.com",
                password: "password@@123"
            })
        })
    })
    it(()=>{
        render(<UserForm/>)
        const submitButon = screen.getByRole('button', {name:/Login/i})
        fireEvent.click(submitButon)

    })
})
