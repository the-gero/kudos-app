// src/pages/HomePage.tsx

import { Button, Container, Grid, Paper, Title } from "@mantine/core";
import SendKudosForm from "./components/SendKudosForm";
import KudosList from "./components/KudosList";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  return (
    <Container size="lg" mt="lg">
      <Title order={2} mb="lg" ta="center" display={"flex"} style={{justifyContent:"space-around"}}>
        Welcome to Kudos!
        <Button
          onClick={() => {
            localStorage.removeItem("token");
            navigate("/login")
          }}
        >
          Logout
        </Button>
      </Title>

      <Grid>
        <Grid.Col span={{ base: 12, md: 6 }}>
          <Paper shadow="xs" p="md" withBorder radius="md">
            <Title order={4} mb="sm">
              Send Kudos
            </Title>
            <SendKudosForm />
          </Paper>
        </Grid.Col>

        <Grid.Col span={{ base: 12, md: 6 }}>
          <Paper shadow="xs" p="md" withBorder radius="md">
            <Title order={4} mb="sm">
              Your Kudos
            </Title>
            <KudosList />
          </Paper>
        </Grid.Col>
      </Grid>
    </Container>
  );
};

export default Home;
