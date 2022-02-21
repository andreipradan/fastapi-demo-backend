CREATE MIGRATION m1zoac4lcwxeh4sw4bkebb7pj6fvbc2ukjonhkmauc5yyig3dg3esa
    ONTO m146ilhwgw4dhegnsi4oeufnt4b66hgfuej3vaqrdgd5p5gmlfy6aq
{
  ALTER TYPE default::Item {
      ALTER PROPERTY name {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
