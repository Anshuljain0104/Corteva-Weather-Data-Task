-- WeatherData definition

CREATE TABLE "WeatherData" (
"index" INTEGER,
  "date" TEXT,
  "max_temperature" REAL,
  "min_temperature" REAL,
  "precipitation" REAL,
  "station_id" TEXT
);

CREATE INDEX "ix_WeatherData_index"ON "WeatherData" ("index");


-- WeatherStats definition

CREATE TABLE "WeatherStats" (
"index" INTEGER,
  "station_id" TEXT,
  "year" TEXT,
  "avg_max_temperature" REAL,
  "avg_min_temperature" REAL,
  "total_precipitation" REAL
);

CREATE INDEX "ix_WeatherStats_index"ON "WeatherStats" ("index");