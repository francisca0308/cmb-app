import useSWR from "swr";
import { requests as requestData } from "./placeholders";

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export interface RequestChat {
  id: number;
  person_id: number;
  module_id: number;
  initial_date: string;
  comment: string;
}

export const useRequestData = () => {
  const { data } = useSWR("/api/products", fetchProducts, {
    suspense: true,
  });

  const request_data = data as RequestChat[];

  return request_data;
};

const fetchProducts = async () => {
  await sleep(1000);
  return requestData;
};
