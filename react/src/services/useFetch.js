import { useState, useRef, useEffect } from "react";
import api from "./api";
import { useAuth } from "./auth";

export default function useFetch(url) {
  const isMounted = useRef(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const { token } = useAuth();

  useEffect(() => {
    isMounted.current = true;
    async function init() {
      try {
        const response = await fetch(api + url, {
          headers: { "X-Auth": token },
        });
        if (response.ok) {
          const json = await response.json();
          if (isMounted.current) setData(json);
        } else {
          throw response;
        }
      } catch (e) {
        if (isMounted.current) setError(e);
      } finally {
        if (isMounted.current) setLoading(false);
      }
    }
    init();

    return () => {
      isMounted.current = false;
    };
  }, [url, token]);

  return { data, error, loading };
}
