// src/components/KudosList.tsx

import { useEffect, useState } from "react";
import { Paper, Text, Title, Stack, Group, Loader } from "@mantine/core";
// import { IconGift } from "@tabler/icons-react";
import { useGetKudosQuery } from "../../../apis/kudos.api";

interface KudoItem {
  from_user: string;
  to_user: string;
  message: string;
}

const KudoCard = ({
  kudo,
  type,
}: {
  kudo: KudoItem;
  type: "sent" | "received";
}) => (
  <Paper withBorder p="md" radius="md" shadow="sm">
    <Group align="center" gap="xs">
      {/* <IconGift size={18} /> */}
      <Text size="sm" fw={500}>
        {type === "sent" ? `To: ${kudo.to_user}` : `From: ${kudo.from_user}`}
      </Text>
    </Group>
    <Text size="sm" mt="xs">
      {kudo.message}
    </Text>
  </Paper>
);

const KudosList = () => {
  const { data, error, isLoading } = useGetKudosQuery();
  const [received, setReceived] = useState<KudoItem[]>([]);
  const [sent, setSent] = useState<KudoItem[]>([]);

  useEffect(() => {
    if (data) {
      setReceived(data.received || []);
      setSent(data.sent || []);
    }
  }, [data]);

  if (isLoading) return <Loader />;

  if (error) return <Text c="red">Failed to load kudos.</Text>;

  return (
    <Stack gap="xl">
      <div>
        <Title order={4}>Sent Kudos</Title>
        <Stack mt="xs">
          {sent.length === 0 ? (
            <Text size="sm" c="dimmed">
              No kudos sent yet.
            </Text>
          ) : (
            sent.map((kudo, i) => <KudoCard key={i} kudo={kudo} type="sent" />)
          )}
        </Stack>
      </div>

      <div>
        <Title order={4}>Received Kudos</Title>
        <Stack mt="xs">
          {received.length === 0 ? (
            <Text size="sm" c="dimmed">
              No kudos received yet.
            </Text>
          ) : (
            received.map((kudo, i) => (
              <KudoCard key={i} kudo={kudo} type="received" />
            ))
          )}
        </Stack>
      </div>
    </Stack>
  );
};

export default KudosList;
