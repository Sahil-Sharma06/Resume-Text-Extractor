import UploadResume from "./components/UploadResume";
import DarkModeToggle from "./components/darkModeToggle"
function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-white transition-all duration-300">
      <div className="absolute top-5 right-5">
        <DarkModeToggle />
      </div>
      <UploadResume />
    </div>
  );
}

export default App;
