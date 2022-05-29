import useSWR from "swr";

import { modules_chat as moduleData } from "./placeholders";

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export interface Module {
  id: number;
  min_profiles: number;
  initial_date: string;
  state: string;
  people: number[];
}

export const useModulesData = () => {
  const { data } = useSWR("/api/products", fetchProducts, {
    suspense: true,
  });

  const modules_chat = data as Module[];

  return modules_chat;
};

const fetchProducts = async () => {
  await sleep(1000);
  return moduleData;
};
