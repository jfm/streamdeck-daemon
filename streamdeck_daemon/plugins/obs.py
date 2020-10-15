import asyncio
import simpleobsws


loop = asyncio.new_event_loop()
obs = simpleobsws.obsws(loop=loop)
request_map = {
        'change_scene': 'SetCurrentScene'
}


def handle_action(logger, view_handler, action_config):
    return loop.run_until_complete(handle_action_async(logger, view_handler, action_config))


def get_request_dictionary(action_config):
    if action_config['request'] == 'change_scene':
        return {'scene-name': action_config['scene']}


async def handle_action_async(logger, view_handler, action_config):
    await obs.connect()
    request = request_map.get(action_config['request'])
    request_data = get_request_dictionary(action_config)
    result = await obs.call(request, data=request_data)
    print(result)
    await obs.disconnect()
    return 'success'



