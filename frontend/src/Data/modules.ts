import useSWR from "swr";

import { modules_chat as moduleData } from "./placeholders";
import { API_URL, get } from "./utils";

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export interface Module {
  id: number;
  min_profiles: number;
  initial_date: string;
  state: number;
  people: number[];
}

export const useModulesData = () => {
  const data2 = get(API_URL);

  const { data } = useSWR("/api/products", fetchProducts, {
    suspense: true,
  });

  const modules_chat = data2 as Module[];

  return modules_chat;
};

const fetchProducts = async () => {
  await sleep(1000);
  return moduleData;
};

export interface ModulePreference {
  id: number;
  initial_date: string;
  preference: number;
}
