import { useState, useEffect } from "react";

import { user as userData } from "./placeholders";

export interface User {
  id: number;
  name: string;
  email: string;
  comunication_of_preference: string;
}

export default function useUserData(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      setUser(userData);
    };
    fetchUser().finally(() => setLoading(false));
  }, [userId]);

  return { user, loading };
}
