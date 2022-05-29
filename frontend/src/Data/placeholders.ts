export const user = {
  id: 1,
  name: "John Doe",
  email: "jhon@gmail.com",
  comunication_of_preference: "slack",
};

export const modules_chat = [
  {
    id: 1,
    min_profiles: 1,
    initial_date: "30/05/2022, 10:00:00 AM",
    state: "green",
    people: [1],
  },
  {
    id: 2,
    min_profiles: 1,
    initial_date: "31/05/2022, 10:00:00 AM",
    state: "yellow",
    people: [2],
  },
  {
    id: 3,
    min_profiles: 1,
    initial_date: "01/06/2022, 10:00:00 AM",
    state: "red",
    people: [1],
  },
];

export const requests = [
  {
    id: 1,
    person_id: 1,
    module_id: 1,
    initial_date: "29/05/2022",
    comment: "Please change my chat watch :)",
  },
];
