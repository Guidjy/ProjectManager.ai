// layout
import LoginRegisterLayout from "../layouts/LoginRegisterLayout";
// components
import { Form, FormField } from "../components/Form";
// services
import { login } from "../services/auth";
// hooks
import { useState } from "react";


export default function LoginPage() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const fields = [
    { label: "Username", type: "text", placeholder: "username", onChange: (event) => {setUsername(event.target.value)} },
    { label: "Password", type: "password", placeholder: "password", onChange: (event) => {setPassword(event.target.value)} },
  ];

  return (
    <>
      <LoginRegisterLayout>
        {/* Login form */}
        <Form
        fields={fields}
        onSubmit={() => login(username, password)}
        />
      </LoginRegisterLayout>
    </>
  );
}