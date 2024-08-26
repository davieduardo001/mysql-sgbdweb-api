# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Build the React app
RUN npm run build

# Install a simple web server to serve the React app
RUN npm install -g serve

# Start the app using serve on port 3000
CMD ["serve", "-s", "build", "-l", "3000"]

