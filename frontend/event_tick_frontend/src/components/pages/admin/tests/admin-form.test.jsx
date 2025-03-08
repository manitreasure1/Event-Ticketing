import {screen, render, fireEvent, waitFor} from '@testing-library/react';
import { describe, it, expect } from 'jest';
import userEvent from '@testing-library/user-event';
import AdminForm from './admin-form';
import { jest } from '@jest/globals';


console.log = jest.fn();

describe("AdminForm Component", () => {
    it("should render the form with lables and inputs", () => {
        render(<AdminForm />);
        expect(screen.getByRole('heading', {name: /admin login/i}).toBeInTheDocument());
        expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
        expect(screen.getByRole('button', {name: /login/i})).toBeInTheDocument();
        
    });
    it("update email and password input value on input change", () => {
        render(<AdminForm/>)
        const emailInput = screen.getByLabelText(/email/i);
        const passwordInput = screen.getByLabelText(/password/i);
        fireEvent.change(emailInput, {target: {value: 'example@email.com'}});
        fireEvent.change(passwordInput, {target: {value:"password@@123"}})
    });
    it("submit the form with correct data", async () => {
        render(<AdminForm/>)
        const emailInput = screen.getByLabelText(/email/i);
        const passwordInput = screen.getByLabelText(/password/i);
        const submitButton = screen.getByRole("button", {name: /Login/i});
        userEvent.type(emailInput, 'example@email.com');
        userEvent.type(passwordInput, 'password@@123');
        fireEvent.click(submitButton);

        await waitFor(()=>{
            expect(console.log).toHaveBeenCalledWith({
                email:"example@email.com",
                password: "password@@123"
            })
        })
    })
    it("prevent submission with empty form", ()=>{
        render(<AdminForm/>)
        const submitButton = screen.getByRole("button", {name:/Login/i});
        fireEvent.click(submitButton);
    })

});

// TODO: Admin DashBoard Test

