from ai_library import validate_config, update_config, show_config
 
#update config (here everything is set very small so that the pipeline can run quickly)
update_config(None,updates=["parquet_train_size", 200])
update_config(None,updates=["pipeline_type", "gmlp"])
update_config(None,updates=["stride", 2])
update_config(None,updates=["window", 2])
update_config(None,updates=["horizon", 2])
update_config(None, updates=["data_frequency","1s"])
#also add the timestamp column to the config exclude columns
update_config(None, updates=["cols_to_drop", ["ts"]])
show_config()
validate_config()

#next step is to start recorder in the terminal
# .env example:
#MON_CLIENT_STOMP_HOST=127.0.0.1
#MON_CLIENT_STOMP_PORT=61622
#run in bash:
#nohup python3 -c "from ai_library import record; record.main()" > record.log 2>&1 & 

#run this after a while when some data is collected (or just run it and after a while it will work)
import ai_library.codebase.setup.cron_manager as cron_manager
#add train to cron
cron_manager.add_to_cron()

from ai_library import train, infer
#run train once manually and infer after training
train()
predictions, first_predicted, last_predicted, data_frequency, conformal_q = infer()
print(predictions, first_predicted, last_predicted, data_frequency, conformal_q)

#cron_manager.remove_from_cron()
