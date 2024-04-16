import gymnasium as gym
from stable_baselines3 import A2C, PPO
import comet_ml
from comet_ml.integration.gymnasium import CometLogger
import io
import ipywidgets as widgets
from IPython.display import display

# Create and display the widget for API key input
api_key_input = widgets.Text(
    value='',
    placeholder='Enter API key here',
    description='API Key:',
    disabled=False,
    continuous_update=False
)

def initialize_comet(api_key):
    comet_ml.config.save(api_key=api_key, force=True)
    comet_ml.init(project_name="comet-examples-gymnasium-notebook")
    print("Comet ML initialized.")

def handle_submit(change):
    if change['type'] == 'change' and change['name'] == 'value':
        initialize_comet(change['new'])

api_key_input.observe(handle_submit, 'value')
display(api_key_input)

def setup_and_run_model():
    experiment = comet_ml.Experiment()

    # Define the environment and enable video recording with explicit FPS setting
    env = gym.make("Acrobot-v1", render_mode="rgb_array")
    env = gym.wrappers.RecordVideo(env, video_folder='video_output', step_trigger=lambda x: x % 100 == 0, video_length=200, fps=30)
    env = CometLogger(env, experiment)

    model = A2C("MlpPolicy", env, verbose=0)
    model.learn(total_timesteps=10000)

    # Optionally log model architecture
    s = io.StringIO()
    print(model.policy, file=s)
    experiment.log_asset(s.getvalue(), file_name="A2C_model_architecture.txt")
    s.close()

    # Optionally log a video file if it exists
    # Update the filename according to your actual output
    experiment.log_asset("video_output/Acrobot-v1.mp4", file_name="Acrobot_training_video.mp4")

    env.close()
    experiment.end()

# Call the function to setup and run the model after API key input
if api_key_input.value:
    setup_and_run_model()
