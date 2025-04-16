import { useState } from "react";
import {
  TextInput,
  PasswordInput,
  Button,
  Paper,
  Title,
  Stack,
  Container,
} from "@mantine/core";
import { useLoginMutation } from "../../apis/auth.api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [login, { isLoading, error }] = useLoginMutation();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async () => {
    try {
      const res = await login({ email, password }).unwrap();
      localStorage.setItem("token", res.token);
      navigate("/")
    } catch (err) {
      console.error("Login failed", err);
    }
  };

  return (
    <Container size={420} my={40}>
      <Title ta="center">Login</Title>
      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <Stack>
          <TextInput
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.currentTarget.value)}
          />
          <PasswordInput
            label="Password"
            value={password}
            onChange={(e) => setPassword(e.currentTarget.value)}
          />
        </Stack>
        <Button fullWidth mt="xl" onClick={handleSubmit} loading={isLoading}>
          Sign in
        </Button>
        {error && <p style={{ color: "red" }}>Login failed</p>}
      </Paper>
    </Container>
  );
}
