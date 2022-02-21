CREATE MIGRATION m146ilhwgw4dhegnsi4oeufnt4b66hgfuej3vaqrdgd5p5gmlfy6aq
    ONTO m1lvniahiwuhimtsstbhb7c6rgj6d7gcq5qdcz53qy4kl3ryt722oq
{
  ALTER TYPE default::Item {
      ALTER PROPERTY is_offer {
          RESET OPTIONALITY;
      };
  };
};
