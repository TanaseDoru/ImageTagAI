
CREATE TABLE ImageTags (
  Id INT IDENTITY(1,1) PRIMARY KEY,
  FileName NVARCHAR(255),
  BlobUrl NVARCHAR(1000),
  Timestamp DATETIME,
  Tag NVARCHAR(100),
  Confidence FLOAT
);
