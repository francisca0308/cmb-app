import { lazy } from "react";

const Home = lazy(() => import("../Controllers/Home"));
const Requests = lazy(() => import("../Controllers/Requests"));
const Modules = lazy(() => import("../Controllers/Modules"));
const Calendar = lazy(() => import("../Controllers/Calendar"));

export const MODULES_LINK = "modules";
export const REQUESTS_LINK = "requests";
export const CALENDAR_LINK = "calendar";

export const appRoutes = [
  { path: "/*", component: Home },
  { path: `/${MODULES_LINK}`, component: Modules },
  { path: `/${REQUESTS_LINK}`, component: Requests },
  { path: `/${CALENDAR_LINK}`, component: Calendar },
];
