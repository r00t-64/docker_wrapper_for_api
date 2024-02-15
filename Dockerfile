# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /${PROJECT_NAME}

# Copy package.json and package-lock.json to the container
COPY ${PROJECT_NAME}/package*.json ./

# Install application dependencies
RUN npm install

# Copy the rest of the application source code to the container
COPY ${PROJECT_NAME}/ ./

# Expose port 
EXPOSE ${PORT}

# Start the application
CMD ["npm", "start"]