import React from "react";
import { Button, Textarea, Select, Card, Title, Stack } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useSendKudosMutation } from "../../../apis/kudos.api";
import { useGetAllUsersQuery } from "../../../apis/auth.api";


const SendKudosForm = () => {
  const { data: users, isLoading } = useGetAllUsersQuery();
  const [sendKudos, { isLoading: isSending }] = useSendKudosMutation();

  const form = useForm({
    initialValues: {
      kudos_to: "",
      kudos_text: "",
    },
    validate: {
      kudos_to: (value) => (value ? null : "Please select a user"),
      kudos_text: (value) =>
        value.trim().length > 0 ? null : "Message cannot be empty",
    },
  });

  const handleSubmit = async (values: typeof form.values) => {
    try {
      await sendKudos(values).unwrap();
      form.reset();
    } catch (err) {
      console.error("Failed to send kudos:", err);
    }
  };

  const userOptions =
    users?.map((user: any) => ({
      label: user.name,
      value: user._id,
    })) || [];

  return (
    <Card shadow="md" radius="md" p="lg" withBorder>
      <Title order={4} mb="md">
        Send Kudos
      </Title>
      <form onSubmit={form.onSubmit(handleSubmit)}>
        <Stack>
          <Select
            label="Send To"
            placeholder="Select a user"
            data={userOptions}
            {...form.getInputProps("kudos_to")}
            disabled={isLoading}
          />

          <Textarea
            label="Message"
            placeholder="Write a nice message"
            minRows={3}
            autosize
            {...form.getInputProps("kudos_text")}
          />

          <Button type="submit" loading={isSending}>
            Send
          </Button>
        </Stack>
      </form>
    </Card>
  );
};

export default SendKudosForm;
