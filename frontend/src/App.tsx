import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./pages/login";
import Protected from "./routes/Protected";
import Home from "./pages/home";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/"
          element={
            <Protected>
              <Home />
            </Protected>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
