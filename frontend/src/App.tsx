import "./App.css";
import { lazy, Suspense } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Spinner from "./Services/Spinner";
import PageNotFound from "./Services/NotFound";
// containers
const AppLayout = lazy(() => import("./Navigation/Layout/AppLayout"));

function App() {
  return (
    <div className="root">
      <BrowserRouter>
        <Suspense fallback={<Spinner />}>
          <Routes>
            <Route path={"/*"} element={<AppLayout />} />
            <Route path="*" element={<PageNotFound />} />
          </Routes>
        </Suspense>
      </BrowserRouter>
    </div>
  );
}

export default App;
