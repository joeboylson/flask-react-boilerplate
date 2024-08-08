import MinimalButton from "../../components/MinimalButton";
import { useCallback } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();

  const handleLogin = useCallback(() => {
    /**
     * TODO: do login here
     */
    navigate("/");
  }, []);

  return (
    <>
      <p>Login Page</p>
      <MinimalButton onClick={handleLogin}>Go to Homepage</MinimalButton>
    </>
  );
}
