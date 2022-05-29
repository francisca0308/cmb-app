import axios from "axios";

interface Props<D> {
  url: string;
  data: D;
}

export const post = ({ url, data }: Props<any>) =>
  axios.post(url, data).then((res) => res);

export const get = (url: string) => axios.get(url).then((res) => res);

export const API_URL = "https://localhost:8000";
