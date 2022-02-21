CREATE MIGRATION m1lvniahiwuhimtsstbhb7c6rgj6d7gcq5qdcz53qy4kl3ryt722oq
    ONTO initial
{
  CREATE TYPE default::Item {
      CREATE REQUIRED PROPERTY is_offer -> std::bool;
      CREATE REQUIRED PROPERTY name -> std::str;
      CREATE REQUIRED PROPERTY price -> std::float32;
  };
};
