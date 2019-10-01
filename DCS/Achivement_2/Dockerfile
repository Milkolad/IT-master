FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src

COPY ["Achivement_2.csproj", "./"]
RUN dotnet restore "Achivement_2.csproj"
COPY . .
WORKDIR "/src"
RUN dotnet build "Achivement_2.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Achivement_2.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Achivement_2.dll"]