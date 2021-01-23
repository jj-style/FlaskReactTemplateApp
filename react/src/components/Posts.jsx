import React from "react";
import useFetch from "../services/useFetch";

const Posts = () => {
  const { data, loading, error } = useFetch("/posts");

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error.statusText}</p>;
  console.log("posts", data);
  return (
    <div>
      <h2>Posts</h2>
      {data.length ? (
        data.map((post, postIdx) => {
          return (
            <div key={postIdx}>
              <p>{post.title}</p>
              <small>written by: {post.author.username}</small>
              <p>{post.body}</p>
            </div>
          );
        })
      ) : (
        <p>No Posts Found</p>
      )}
    </div>
  );
};

export default Posts;
