
import {screen, render, fireEvent, waitFor} from '@testing-library/react';
import { describe, it, expect } from 'jest';
import userEvent from '@testing-library/user-event';
import { jest } from '@jest/globals';
import RegisterOrg from '../register-org';


console.log = jest.fn()

describe("OraganizationForm Components", ()=>{
    it("render valid lable and user input",()=>{
        render(<RegisterOrg/>);
        expect(screen.getByRole('legend', {name: /Register Organization/i}))
        expect(screen.getByLabelText(/name/i)).toBeInTheDocument()
        expect(screen.getByLabelText(/email/i)).toBeInTheDocument()
        expect(screen.getByLabelText(/description/i)).toBeInTheDocument()

    })
   
})