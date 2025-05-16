#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python -m chainlit run chainlit_app/main.py --host 0.0.0.0 --port $PORT
