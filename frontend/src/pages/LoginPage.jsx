// layout
import LoginRegisterLayout from "../layouts/LoginRegisterLayout";
// components
import { Form, FormField } from "../components/Form";


export default function LoginPage() {

  const fields = [
    { label: "Username", type: "text", placeholder: "username" },
    { label: "Password", type: "password", placeholder: "password" },
  ];

  return (
    <>
      <LoginRegisterLayout>
        {/* Login form */}
        <Form
        fields={fields}
        onSubmit={() => {console.log('form submitted');} }
        />
      </LoginRegisterLayout>
    </>
  );
}