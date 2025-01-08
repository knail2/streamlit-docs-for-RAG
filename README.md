# streamlit-docs-for-RAG
LLMs cant keep up with streamlit versions, so I'm writing this code to download all the latest streamlit documents and convert them to pdf so I can use RAG with my LLMs to write streamlit code using their latest libraries


## how to use
```
python -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install  
cd code
python download-st-docs-v2.py
```



## execution and data extracted

the following documentation is downloaded into /data

you can RAG this and turbocharge your fav LLM to use the latest streamlit code to write, and stop running into the experimental functions that the stale pretrained LLM data uses to write code for you.

```
python -u "/Users/knail1/code/knail2/streamlit-doctcm streamlit-docs-for-RAG$ s-for-RAG/code/download-streamlit-docs.py"
python -u "/Users/knail1/code/knail2/streamlit-docs-for-RAG/code/download-streamlit-docs.py"
ic| output_dir: '../data'
ic| response.status_code: 200
ic| len(soup): 2
ic| len(links): 448
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/api-reference.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/api-reference.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/write-magic.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/write-magic.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/text.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/text.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/data.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/data.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/charts.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/charts.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/widgets.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/widgets.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/media'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/media.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/media.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/layout.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/layout.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/chat'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/chat.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/chat.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/status.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/status.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/navigation'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/navigation.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/navigation.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/execution-flow.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/execution-flow.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/caching-and-state'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/caching-and-state.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/caching-and-state.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/connections.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/connections.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/custom-components'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/custom-components.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/custom-components.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/utilities'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/utilities.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/utilities.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/configuration'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/configuration.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/configuration.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/app-testing.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/app-testing.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/cli'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/cli.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/cli.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/api-reference.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/api-reference.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/st.write'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.write.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.write.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.write_stream.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.write_stream.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/magic'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/magic.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/magic.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.markdown'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.markdown.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.markdown.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.title'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.title.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.title.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.header'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.header.pdf'
Traceback (most recent call last):
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/code/download-streamlit-docs.py", line 63, in <module>
    html_to_pdf(sub_response.text, pdf_file_path)
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/code/download-streamlit-docs.py", line 28, in html_to_pdf
    page.set_content(html_content)
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/venv/lib/python3.11/site-packages/playwright/sync_api/_generated.py", line 8938, in set_content
    self._sync(
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/venv/lib/python3.11/site-packages/playwright/_impl/_sync_base.py", line 115, in _sync
    return task.result()
           ^^^^^^^^^^^^^
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/venv/lib/python3.11/site-packages/playwright/_impl/_page.py", line 542, in set_content
    return await self._main_frame.set_content(**locals_to_params(locals()))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/venv/lib/python3.11/site-packages/playwright/_impl/_frame.py", line 424, in set_content
    await self._channel.send("setContent", locals_to_params(locals()))
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/venv/lib/python3.11/site-packages/playwright/_impl/_connection.py", line 61, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/knail1/code/knail2/streamlit-docs-for-RAG/venv/lib/python3.11/site-packages/playwright/_impl/_connection.py", line 528, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.TimeoutError: Page.set_content: Timeout 30000ms exceeded.
Call log:
  - setting frame content, waiting until "load"

tcm streamlit-docs-for-RAG$ python -u "/Users/knail1/code/knail2/streamlit-docs-for-RAG/code/download-st-docs-v2.py"
ic| output_dir: '../data'
ic| response.status_code: 200
ic| len(soup): 2
ic| len(links): 448
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/api-reference.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/api-reference.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/write-magic.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/write-magic.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/text.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/text.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/data.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/data.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/charts.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/charts.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/widgets.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/widgets.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/media'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/media.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/media.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/layout.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/layout.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/chat'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/chat.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/chat.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/status.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/status.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/navigation'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/navigation.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/navigation.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/execution-flow.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/execution-flow.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/caching-and-state'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/caching-and-state.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/caching-and-state.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/connections.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/connections.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/custom-components'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/custom-components.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/custom-components.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/utilities'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/utilities.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/utilities.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/configuration'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/configuration.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/configuration.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/app-testing.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/app-testing.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/cli'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/cli.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/cli.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/api-reference.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/st.write'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.write.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.write.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.write_stream.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.write_stream.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/magic'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/magic.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/magic.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.markdown'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.markdown.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.markdown.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.title'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.title.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.title.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.header'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.header.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.header.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.subheader'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.subheader.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.subheader.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.caption'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.caption.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.caption.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.code'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.code.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.code.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.echo'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.echo.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.echo.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.latex'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.latex.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.latex.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.text'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.text.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.text.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/text/st.divider'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.divider.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.divider.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.dataframe'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.dataframe.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.dataframe.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.data_editor'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.data_editor.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.data_editor.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.column_config'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.column_config.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.column_config.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.table'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.table.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.table.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.metric'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.metric.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.metric.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.json'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.json.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.json.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.area_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.area_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.area_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.bar_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.bar_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.line_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.line_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.line_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.scatter_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.scatter_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.map'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.map.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.map.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.pyplot'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.pyplot.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.pyplot.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.altair_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.altair_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.vega_lite_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.vega_lite_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.vega_lite_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.plotly_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.plotly_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.bokeh_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.bokeh_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.bokeh_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.pydeck_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.pydeck_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/charts/st.graphviz_chart'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.graphviz_chart.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.graphviz_chart.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.button'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.button.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.button.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.download_button'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.download_button.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.download_button.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.form_submit_button.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.form_submit_button.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.link_button'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.link_button.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.link_button.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.page_link'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.page_link.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.page_link.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.checkbox.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.checkbox.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.color_picker.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.color_picker.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.feedback'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.feedback.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.feedback.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.multiselect.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.multiselect.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.pills'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.pills.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.pills.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.radio'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.radio.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.radio.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.segmented_control'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.segmented_control.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.segmented_control.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.selectbox.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.selectbox.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.select_slider'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.select_slider.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.select_slider.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.toggle'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.toggle.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.toggle.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.number_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.number_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.number_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.slider'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.slider.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.slider.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.date_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.date_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.date_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.time_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.time_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.time_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/chat/st.chat_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.chat_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.chat_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.text_area'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.text_area.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.text_area.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.text_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.text_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.text_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.audio_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.audio_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.audio_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/data/st.data_editor'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/st.data_editor.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.file_uploader.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.file_uploader.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.camera_input'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.camera_input.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.camera_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/media/st.image'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.image.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.image.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/media/st.logo'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.logo.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.logo.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/media/st.audio'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.audio.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.audio.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/media/st.video'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.video.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.video.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.columns'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.columns.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.columns.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.container'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.container.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.container.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.dialog.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.dialog.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.empty'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.empty.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.empty.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.expander'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.expander.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.expander.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.popover'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.popover.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.popover.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.sidebar'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.sidebar.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.sidebar.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/layout/st.tabs'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.tabs.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.tabs.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/chat/st.chat_input'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/st.chat_input.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/chat/st.chat_message'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.chat_message.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.chat_message.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.status'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.status.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.status.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/st.write_stream.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.progress'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.progress.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.progress.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.spinner'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.spinner.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.spinner.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.status'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/st.status.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.toast'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.toast.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.toast.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.balloons'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.balloons.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.balloons.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.snow'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.snow.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.snow.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.success'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.success.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.success.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.info'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.info.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.info.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.warning'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.warning.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.warning.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.error'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.error.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.error.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/status/st.exception'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.exception.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.exception.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/navigation/st.navigation'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.navigation.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.navigation.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/navigation/st.page'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.page.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.page.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/widgets/st.page_link'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/st.page_link.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.switch_page.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.switch_page.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/st.dialog.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.form'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.form.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.form.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.fragment.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.fragment.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.rerun.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.rerun.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/execution-flow/st.stop'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.stop.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.stop.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.cache_data.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.cache_data.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.cache_resource.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.cache_resource.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.session_state.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.session_state.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.query_params.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.query_params.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections/st.connection'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.connection.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.connection.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowflakeconnection'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.connections.snowflakeconnection.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.connections.snowflakeconnection.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections/st.connections.sqlconnection'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.connections.sqlconnection.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.connections.sqlconnection.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections/st.connections.baseconnection'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.connections.baseconnection.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.connections.baseconnection.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections/st.secrets'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.secrets.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.secrets.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/connections/secrets.toml'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/secrets.toml.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/secrets.toml.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.declare_component'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.components.v1.declare_component.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.components.v1.declare_component.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.components.v1.html.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.components.v1.html.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.iframe'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.components.v1.iframe.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.components.v1.iframe.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/utilities/st.context'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.context.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.context.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/utilities/st.help'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.help.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.help.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/utilities/st.html'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.html.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.html.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/utilities/st.experimental_user'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.experimental_user.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.experimental_user.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/configuration/config.toml'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/config.toml.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/config.toml.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/configuration/st.get_option'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.get_option.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.get_option.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/configuration/st.set_option'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.set_option.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.set_option.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.set_page_config.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.set_page_config.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.testing.v1.apptest.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.testing.v1.apptest.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.testing.v1.apptest#apptestfrom_file.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.testing.v1.apptest#apptestfrom_file.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_string'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.testing.v1.apptest#apptestfrom_string.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.testing.v1.apptest#apptestfrom_string.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/st.testing.v1.apptest#apptestfrom_function.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/st.testing.v1.apptest#apptestfrom_function.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treeblock.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treeblock.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeelement'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treeelement.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treeelement.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treebutton.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treebutton.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treechatinput'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treechatinput.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treechatinput.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecheckbox'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treecheckbox.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treecheckbox.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecolorpicker'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treecolorpicker.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treecolorpicker.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treedateinput'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treedateinput.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treedateinput.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treemultiselect'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treemultiselect.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treemultiselect.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treenumberinput'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treenumberinput.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treenumberinput.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeradio'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treeradio.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treeradio.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectslider'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treeselectslider.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treeselectslider.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectbox'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treeselectbox.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treeselectbox.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeslider'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treeslider.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treeslider.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextarea'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treetextarea.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treetextarea.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextinput'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treetextinput.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treetextinput.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetimeinput'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treetimeinput.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treetimeinput.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetoggle'
ic| sub_response.status_code: 200
ic| pdf_file_path: '../data/testing-element-classes#sttestingv1element_treetoggle.pdf'
ic| f"Saved {pdf_file_path}": 'Saved ../data/testing-element-classes#sttestingv1element_treetoggle.pdf'
ic| subpage_url: 'https://docs.streamlit.io/develop/api-reference/write-magic'
ic| sub_response.status_code: 200
ic| f"Skipping already downloaded: {pdf_file_path}": 'Skipping already downloaded: ../data/write-magic.pdf'
Downloaded and converted Streamlit docs to PDF in ../data
tcm streamlit-docs-for-RAG$ 
```